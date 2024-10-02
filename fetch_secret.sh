for secret in $(oc get secrets --all-namespaces -o jsonpath='{range .items[?(@.type=="kubernetes.io/dockerconfigjson")]}{.metadata.namespace}{" "}{.metadata.name}{"\n"}{end}'); do
  namespace=$(echo $secret | awk '{print $1}')
  secret_name=$(echo $secret | awk '{print $2}')
  if oc get secret $secret_name -n $namespace -o jsonpath='{.data.\.dockerconfigjson}' | base64 -d | grep -q 'xyz'; then
    echo "User xyz found in secret $secret_name in namespace $namespace"
  fi
done
