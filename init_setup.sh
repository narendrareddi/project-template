echo [$(date)]: "START"
echo [$(date)]: "Create conda environment with python 3.12"
conda create --prefix ./.venv python=3.12 -y
echo [$(date)]: "Activating environment"
source activate ./.venv
echo [$(date)]: "Installing required packages"
pip install -r requirements.txt
echo [$(date)]: "END"
 
