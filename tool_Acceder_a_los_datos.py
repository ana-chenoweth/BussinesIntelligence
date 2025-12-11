import pandas as pd
import json
from pydantic import Field


class Tools:
    tool_type = "code"
    df_cache = None

    def __init__(self, dataframe: pd.DataFrame = None):
        if Tools.df_cache is None:
            Tools.df_cache = pd.read_csv("/app/datos/datos.csv")
        self.df = Tools.df_cache
        self.df["Transaction date"] = pd.to_datetime(self.df["Transaction date"])

    def run_pandas_code(
        self,
        code: str = Field(
            ...,
            description="Código Pandas de UNA SOLA LÍNEA para ejecutar sobre el DataFrame df. Debe retornar un DataFrame, Series o valor escalar.",
        ),
    ) -> str:
        try:
            safe_locals = {"df": self.df, "pd": pd}
            result = eval(code, {"__builtins__": {}}, safe_locals)

            if isinstance(result, pd.DataFrame):
                return result.to_json(orient="records")

            if isinstance(result, pd.Series):
                return result.to_json()

            return json.dumps({"result": result})

        except Exception as e:
            return json.dumps({"error": str(e)})
