# analysis-environment

Base repository for data analytsis

## Requirements

OS: Ubuntu

## How to install

### Python

以下の手順に従って Python 環境を構築してください。

1. 以下のようにして、必要モジュールをインストールしてください。

    ```shell
    sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    ```

1. 以下のコマンドを実行して pyenv をインストールしてください。

    ```shell
    curl https://pyenv.run | bash
    ```

1. 以下のコマンドを実行して Python の仮想環境をインストールしてください。

    ```shell
    pyenv install 3.9.9
    ```

1. 以下のコマンドを実行して Python の仮想環境を有効化してください。

    ```shell
    pyenv local 3.9.9
    ```

### Poetry

本リポジトリでは [Poetry](https://python-poetry.org/) を使ってパッケージ管理を行います。以下の手順に従って依存関係をインストールしてください。

1. [公式ドキュメント](https://python-poetry.org/docs/)に従って Poetry をインストールしてください。

1. 以下のコマンドを実行して依存するパッケージをインストールしてください。

    ```shell
    poetry install
    ```

1. 以下のコマンドを実行して Poetry の仮想環境をアクティベートしてください。

    ```shell
    poetry shell
    ```

1. Poetry の仮想環境を終了するには以下のコマンドを実行してください。

    ```shell
    exit
    ```

### Nox

本リポジトリでは [Nox](https://nox.thea.codes/en/stable/) を使って仮想環境の構築を含めたコードの半自動テストを行います。以下の手順に従って、コードの lint と test が行われることを確認します。`poetry install`, `poetry shell` が済んだ状態で以下の手順に従ってください。

1. 以下のコマンドを実行すると Nox による半自動テストが行われます。

    ```shell
    nox
    ```

### Documentation

本リポジトリでは [MkDocs](https://www.mkdocs.org) と [mkdocstrings](https://mkdocstrings.github.io) を使って Python の docstrings からドキュメントを自動生成します。`poetry install`, `poetry shell` が済んだ状態で以下の手順に従ってください。

1. 以下のコマンドを実行して MkDocs のビルドが可能です。

    ```shell
    mkdocs build
    ```

    実行後に site ディレクトリが作成され、`site/index.html` をブラウザで読み込むことでドキュメントを読むことができます。

2. また以下のコマンドを実行することで、ブラウザが自動的に立ち上がりファイルの変更に応じて自動的にページが更新されるようになります。

    ```shell
    mkdocs serve
    ```
