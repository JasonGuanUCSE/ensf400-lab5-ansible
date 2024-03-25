import ansible_runner
import requests 

def main():

    command = "ansible-playbook " + "hello.yml"
    result = ansible_runner.interface.run_command(executable_cmd=command)

    response, err_string, rtn_code = result
    print(f"Response: {response}")
    print(f"Return code: {rtn_code}")

    exp_resp1 = "Hello World from managedhost-app-1 !"
    exp_resp2 = "Hello World from managedhost-app-2 !"
    exp_resp3 = "Hello World from managedhost-app-3 !"

    exp_list = [exp_resp1, exp_resp2, exp_resp3]

    for i in range(3):
        response = requests.get('http://0.0.0.0')
        if response.text in exp_list:
            print("Response matched", response.text)
        else:
            print('Expected', exp_list[i], 'actual:', response.text )


if __name__ == "__main__":
    main()