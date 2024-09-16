from datetime import datetime
from pytz import timezone

def main() -> None:
    timezone_br = timezone('America/Sao_Paulo')
    data_atual = datetime.now(timezone_br)
    data_timestamp = data_atual.timestamp()
    print(data_timestamp)
    print(data_atual)

if __name__ == '__main__':
    main()