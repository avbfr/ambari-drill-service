# ambari-drill-service

Ambari service for Apache Drill v0.9-BETA1

Ambari service to run and manage Apache Drill. For more information about Apache Drill visit <a href>https://drill.apache.org/</a>

  Requirements: <br>
    - RHEL/CENTOS 7.1+ <br>
    - Ambari 2.x <br>
    - HDP 2.6 <br>
    - You need HDFS and Zookeeper up & running on your cluster
    
  Features: <br>
    - Allows to install Apache Drill on an Ambari-managed cluster <br>
    - Edit drill-overrides.conf and drill-env.sh via ambari <br>
    - Integration with zookeeper <br>
    - Drill Console Quick Links<br>
    - Choose wich version of drill you want to install (by default 1.14.0)<br>

### Setup

Download the Drill Service:

<code>
git clone https://github.com/avbfr/ambari-drill-service.git /var/lib/ambari-server/resources/stacks/HDP/2.6/services/DRILL 
</code>

Restart ambari

<code>
ambari-server restart
</code>

Now you can install Drill by clicking on "Add Service" button in Ambari

### Uninstall

Stop the Drill Service from Ambari and delete Service

- Delete "drill_install_dir" and "drill_run_dir"
- Keep "drill_config_dir" if you want to install a new version otherwise, delete it
- Delete "drill_temp_file"
