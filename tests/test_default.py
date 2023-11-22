from wake.testing import *

from pytypes.contracts.Dungeon import Dungeon

'''
    Write your exploit here. Always act like in production,
    do not alter the chain anyhow.
'''
def exploit(dungeon: Dungeon, hackeer: Account):
    pass


def subtitles(tx: TransactionAbc):
    for event in tx.events:
        if isinstance(event, Dungeon.Subtitles):
            print(f"--- {event.subtitles} ---")


def revert_handler(e: TransactionRevertedError):
    if e.tx is not None:
        print(e.tx.call_trace)
        print(e.tx.console_logs)


@default_chain.connect()
@on_revert(revert_handler)
def test_hackee():
    default_chain.set_default_accounts(default_chain.accounts[0])
    default_chain.tx_callback = subtitles
    dungeon_master=default_chain.accounts[1] # do not touch
    hackeer=default_chain.accounts[2] # this is you

    dungeon = Dungeon.deploy(from_=dungeon_master)

    exploit(dungeon, hackeer)

    print(f"You managed to gain: {dungeon.evaluate(hackeer)} dungeon tokens.")