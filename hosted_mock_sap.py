from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SAP Mock API", description="Mock SAP OData API for testing")

# Enable CORS for web access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample SAP data
SALES_ORDERS = [
    {
        "SalesOrder": "5000001",
        "SalesOrderType": "OR",
        "SoldToParty": "100001",
        "SalesOrderDate": "2024-01-15T00:00:00",
        "OverallSDProcessStatus": "C",
        "TotalNetAmount": "1500.00",
        "TransactionCurrency": "USD",
        "CreatedByUser": "USER001",
        "CreationDate": "2024-01-15",
        "CompanyCode": "1000"
    },
    {
        "SalesOrder": "5000002",
        "SalesOrderType": "OR",
        "SoldToParty": "100002",
        "SalesOrderDate": "2024-01-16T00:00:00",
        "OverallSDProcessStatus": "B",
        "TotalNetAmount": "2500.00",
        "TransactionCurrency": "USD",
        "CreatedByUser": "USER002",
        "CreationDate": "2024-01-16",
        "CompanyCode": "1000"
    },
    {
        "SalesOrder": "5000003",
        "SalesOrderType": "OR",
        "SoldToParty": "100003",
        "SalesOrderDate": "2024-01-17T00:00:00",
        "OverallSDProcessStatus": "A",
        "TotalNetAmount": "3200.00",
        "TransactionCurrency": "EUR",
        "CreatedByUser": "USER003",
        "CreationDate": "2024-01-17",
        "CompanyCode": "2000"
    }
]

MATERIALS = [
    {
        "Material": "MAT001",
        "MaterialDescription": "Laptop Computer",
        "MaterialType": "ZMAT",
        "BaseUnit": "PC",
        "StandardPrice": "1200.00",
        "PricingUnit": "1"
    },
    {
        "Material": "MAT002",
        "MaterialDescription": "Wireless Mouse",
        "MaterialType": "ZMAT",
        "BaseUnit": "PC",
        "StandardPrice": "25.00",
        "PricingUnit": "1"
    }
]

CUSTOMERS = [
    {
        "Customer": "100001",
        "CompanyName": "ABC Corporation",
        "Country": "US",
        "Currency": "USD",
        "PaymentTerms": "Z001",
        "CreditLimit": "50000.00",
        "Industry": "Technology"
    },
    {
        "Customer": "100002",
        "CompanyName": "XYZ Industries",
        "Country": "DE",
        "Currency": "EUR",
        "PaymentTerms": "Z002",
        "CreditLimit": "75000.00",
        "Industry": "Manufacturing"
    }
]

@app.get("/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder")
async def get_sales_orders():
    """Return sales orders in SAP OData v2 format"""
    return {
        "d": {
            "results": SALES_ORDERS
        }
    }

@app.get("/sap/opu/odata/sap/API_MATERIAL_SRV/A_Material")
async def get_materials():
    """Return materials in SAP OData v2 format"""
    return {
        "d": {
            "results": MATERIALS
        }
    }

@app.get("/sap/opu/odata/sap/API_BP_CUSTOMER_SRV/A_Customer")
async def get_customers():
    """Return customers in SAP OData v2 format"""
    return {
        "d": {
            "results": CUSTOMERS
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "SAP Mock API"}

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "SAP Mock API",
        "version": "1.0",
        "endpoints": [
            "/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder",
            "/sap/opu/odata/sap/API_MATERIAL_SRV/A_Material",
            "/sap/opu/odata/sap/API_BP_CUSTOMER_SRV/A_Customer",
            "/health"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)