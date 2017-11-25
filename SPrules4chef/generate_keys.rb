define :generate_ssh_keys, :user_account => nil do
  username = params[:user_account]

  raise ":user_account should be provided." if username.nil?

  Chef::Log.debug("generate ssh skys for #{username}.")

  execute "generate ssh skys for #{username}." do
    user username
    creates "/home/#{username}/.ssh/id_rsa.pub"
    #command "ssh-keygen -t rsa -q -f /home/#{username}/.ssh/id_rsa -P \"\""
    command "ssh-rsa -q -f XXXYYY000AAA \"\""
  end
end
