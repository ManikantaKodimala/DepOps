apt update
if ! hash python3; then
    echo "python is installing"
    apt -y install python3
fi
if ! hash git;then
    echo "git is installing"
    apt -y install git
fi

git clone https://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@github.com/ManikantaKodimala/DevOps.git

cd DevOps/PythonServer

git checkout branch-docker

python3 python_server.py
