from platform import system
from pprint import pp

from rich.console import Console
from steam.client import SteamClient

console = Console()


def USFget(appIDs: list[int]):
    client = SteamClient()

    with console.status(
        " [bold green]Connecting to Steam; [bold red]⚠️  If it takes too long, check your connection.[/bold red] "
    ) as _:
        client.anonymous_login()

    res = client.get_product_info(appIDs)
    assert res is not None

    return [v["ufs"] for v in res["apps"].values()]


def getOS() -> str:
    return "MacOS" if system() == "macOS" else system()


pp(USFget([1030300]))
