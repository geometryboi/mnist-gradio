from bootstrap.container import Container

if __name__ == "__main__":
    app = Container().build_app()
    app.launch(server_name="0.0.0.0", server_port=7860)
