"""Shared configuration helpers for examples and scripts."""

from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(slots=True)
class AzureContainerAppsConfig:
    """Environment variables used by the deployment examples."""

    environment_name: str = os.getenv("AZURE_CONTAINERAPPS_ENVIRONMENT", "")
    resource_group: str = os.getenv("AZURE_RESOURCE_GROUP", "")
    image_name: str = os.getenv("AZURE_IMAGE_NAME", "")


@dataclass(slots=True)
class DemoApiConfig:
    """Small placeholder for future public API bindings."""

    base_url: str = os.getenv("DEMO_API_BASE_URL", "")
    timeout_seconds: int = int(os.getenv("DEMO_API_TIMEOUT", "30"))
