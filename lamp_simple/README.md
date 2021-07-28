Building a simple LAMP stack and deploying Application using Ansible Playbooks.
-------------------------------------------

These playbooks require Ansible 1.2.

These playbooks are meant to be a reference and starter's guide to building
Ansible Playbooks. These playbooks were tested on CentOS 6.x so we recommend
that you use CentOS or RHEL to test these modules.

This LAMP stack can be on a single node or multiple nodes. The inventory file
'hosts' defines the nodes in which the stacks should be configured.

        [webservers]
        localhost

        [dbservers]
        bensible

Here the webserver would be configured on the local host and the dbserver on a
server called `bensible`. The stack can be deployed using the following
command:

        ansible-playbook -i hosts site.yml

Once done, you can check the results by browsing to http://localhost/index.php.
You should see a simple test page and a list of databases retrieved from the
database server.

        ansible-playbook -i hosts site.yml -t web
        注：-t 指向要执行的模块


注：写完*.yaml文件后可以用下面命令检查语法是否正确。   
例如1.ansible-playbook nginx.yaml --syntax-check

2.使用--list-task、--list-hosts查看所有task和host

3.只运行task里的某个任务
ansible-playbook -i hosts nginx.yaml -f 3 --start-at-task='yum nginx'   (taskr任务名)

4.
