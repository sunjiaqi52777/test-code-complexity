
import subprocess

def run_multimetric(path):
    # Run the multimetric command-line tool using subprocess
    result = subprocess.run(['multimetric', path], stdout=subprocess.PIPE, text=True)
    
    # Capture the output
    output = result.stdout
    
    # Print or return the output as needed
    print(output)



import lizard



def get_cyclomatic_complexity(chunk: dict) -> float:
    """
    Calculates average cyclomatic complexity score.
    Score is calculated for each function, return average if multiple fuctions are detected.

    Args:
        chunk (`dict`): dictionary with chunk data

    Return:
        (`float`): average cyclomatic complexity score
    """
    if chunk["language"].lower() == "python":
        extention = ".py"
    elif chunk["language"].lower() == "java":
        extention = ".java"
    else:
        raise NotImplementedError(
            f"Code complexity calculation for {chunk['language']} language is not implemented"
        )

    comp_res = lizard.analyze_file.analyze_source_code(
        f"file{extention}", chunk["content"]
    )
    return comp_res.average_cyclomatic_complexity



# Example usage:
# Analyze a single Python file
path = "C:\\Users\\JiaQiSun\\Desktop\\test-complexity.java"
chunk = {"content": """
begin int x, y, power;
      float z;
      input(x, y);
      if(y<0)
      power = -y;
      else power = y;
      z=1;
      while(power!=0)
      {    z=z*x;
           power=power-1;
      } if(y<0)
      z=1/z;
      output(z);
      end
        """, 
        "language": "java"}
run_multimetric(path)
res = get_cyclomatic_complexity(chunk=chunk)
print(res)
