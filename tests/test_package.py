"""Package smoke tests."""

from __future__ import annotations

from object_sim import get_asset_root, resolve_asset


def test_asset_root_exists() -> None:
    root = get_asset_root()
    assert root.exists()
    assert (root / "README.md").exists()


def test_can_resolve_known_xml() -> None:
    xml_path = resolve_asset("common.xml")
    assert xml_path.exists()
