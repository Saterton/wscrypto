import _thread as thread
import os
import sys
import time

import websocket

WEBSOCKET_URL = 'wss://stream.binance.com:9443/ws/{symbol}@aggTrade'
RECONNECT_TIME = 5


class WebSocketFile(websocket.WebSocketApp):
    def __init__(self, file=None, *args, **kwargs):
        self.file = file
        super().__init__(
            on_message=self._on_message,
            on_error=self._on_error,
            on_open=self._on_open,
            on_close=self._on_close, *args, **kwargs
        )

    def _on_message(self, message):
        print(message, file=self.file)

    def _on_error(self, error):
        print(error)

    def _on_close(self):
        print('WebSocket closed!')

    def _on_open(self):
        print('WebSocket open!')


def create_directory(filename):
    head, tail = os.path.split(filename)
    if head and not os.path.exists(head):
        os.makedirs(head)


def run_socket(ws):
    while True:
        ws.run_forever()
        time.sleep(RECONNECT_TIME)


def ws_crypto(market_currency, target_currency, work_time, filename):
    try:
        work_time = int(work_time)
    except ValueError:
        print('Work time must be integer')
        return

    try:
        create_directory(filename)
    except OSError as error:
        print(error)
        return

    symbol = (market_currency + target_currency).lower()

    file = open(filename, 'w+')
    ws = WebSocketFile(url=WEBSOCKET_URL.format(symbol=symbol), file=file)
    try:
        thread.start_new_thread(run_socket, (ws,))
        time.sleep(work_time)
    except (Exception, KeyboardInterrupt, SystemExit):
        exit()
    finally:
        ws.close()
        file.close()


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        ws_crypto(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print('Arguments are not enough!')
