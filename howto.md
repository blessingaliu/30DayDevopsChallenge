## 🛠️ Setting Up Your Local Git Repo

Follow these steps to set up a local Git repository for the challenge:

1. **Create a new folder** for your project:

    ```bash
    mkdir examplefolder
    cd examplefolder
    ```

2. **Initialize the Git repository**:

    ```bash
    git init
    ```

3. **Create a README.md file**:

    ```bash
    touch README.md
    ```

4. **Add files to the staging area**:

    ```bash
    git add .
    ```

5. **Commit your changes**:

    ```bash
    git commit -m 'first commit'
    ```

6. **Add the remote repository**:

    ```bash
    git remote add origin https://github.example.git
    ```

7. **Verify the remote URL**:

    ```bash
    git remote -v
    ```

8. **Push your local commits** to the remote GitHub repository:

    ```bash
    git push -u origin main
    ```
