# selecting-lesson-fast

A tool to automate course selection, refactored for maintainability and ease of use.

## Features

-   **Command-Line Interface:** Easy to use with command-line arguments.
-   **Automated Login:** Uses OCR to bypass captchas.
-   **Flexible Course Selection:** Select courses by their ID and plate.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/selecting-lesson-fast.git
    cd selecting-lesson-fast
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. You may also need to install the appropriate WebDriver for your browser. For example, if you are using Chrome, you will need to download ChromeDriver.

## Usage

Run the script from your terminal using the following command:

```bash
python src/main.py --username YOUR_USERNAME --password YOUR_PASSWORD --course-id COURSE_ID --plate PLATE
```

-   `--username`: Your student ID.
-   `--password`: Your password.
-   `--course-id`: The ID of the course you want to select (e.g., `kcmcGrid_xk_4`).
-   `--plate`: The plate of the course you want to select (e.g., `板块（1）`).

### Example

```bash
python src/main.py --username 123456 --password "mysecretpassword" --course-id "kcmcGrid_xk_4" --plate "板块（1）"
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.