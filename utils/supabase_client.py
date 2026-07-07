"""
Supabase database client for Skills Without Borders
"""
import streamlit as st
from supabase import create_client, Client
from typing import Optional, Dict, Any
import json
from datetime import datetime

class SupabaseClient:
    """Singleton Supabase client manager"""
    _instance = None
    _client: Optional[Client] = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def get_client(self) -> Client:
        if self._client is None:
            try:
                from config import Config
                self._client = create_client(
                    Config.SUPABASE_URL,
                    Config.SUPABASE_KEY
                )
            except Exception as e:
                st.error(f"Failed to connect to Supabase: {str(e)}")
                raise
        return self._client
    def execute_query(self, table: str, operation: str, data: Dict = None, filters: Dict = None) -> Dict:
        client = self.get_client()
        try:
            query = client.table(table)
            if operation == "insert":
                result = query.insert(data).execute()
            elif operation == "select":
                if filters:
                    query = query.select("*")
                    for key, value in filters.items():
                        query = query.eq(key, value)
                result = query.execute()
            elif operation == "update":
                if filters:
                    query = query.update(data)
                    for key, value in filters.items():
                        query = query.eq(key, value)
                result = query.execute()
            elif operation == "delete":
                if filters:
                    query = query.delete()
                    for key, value in filters.items():
                        query = query.eq(key, value)
                result = query.execute()
            else:
                raise ValueError(f"Unsupported operation: {operation}")
            return {"success": True, "data": result.data, "error": None}
        except Exception as e:
            return {"success": False, "data": None, "error": str(e)}

# Global instance
_supabase_client = SupabaseClient()

def get_supabase_client() -> Client:
    return _supabase_client.get_client()

def execute_query(table: str, operation: str, data: Dict = None, filters: Dict = None) -> Dict:
    return _supabase_client.execute_query(table, operation, data, filters)
