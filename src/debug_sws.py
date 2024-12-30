from dotenv import load_dotenv
from data_collectors.simply_wall_st import SimplyWallStCollector
import os

load_dotenv()

print(f"SWS_API_TOKEN: {os.getenv('SWS_API_TOKEN')}")

collector = SimplyWallStCollector()
data = collector.get_company_data('NVDA')
