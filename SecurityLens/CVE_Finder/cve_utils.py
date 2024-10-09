import requests
from langchain.tools import BaseTool

class FetchCVEData(BaseTool):
    name = "fetch_cve"
    description = "Fetch CVE data from NVD API using a CVE ID or a keyword."

    def _run(self, query: str):
        # Initialize parameters
        params = {
            'resultsPerPage': 10,  # Limit to 10 results per request
            'startIndex': 0,       # Start from the first result
        }
        if "CVE-" in query:
            # If the query contains a CVE ID, search by ID
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={query}"
        else:
            # Otherwise, treat it as a keyword search
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={query}"
        
        response = requests.get(url,params=params)
        data = response.json()
        
        # Extract and format the results
        if 'vulnerabilities' in data:
            results = []
            for item in data['vulnerabilities']:
                cve_id = item['cve']['id']
                description = item['cve']['descriptions'][0]['value']
                results.append(f"{cve_id}: {description}")
            return "\n".join(results)
        else:
            return "No CVEs found."

    def _arun(self, query: str):
        raise NotImplementedError("Async not supported")
