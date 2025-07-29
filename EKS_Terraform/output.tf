output "cluster_id" {
  value = aws_eks_cluster.anushkachavan20.id
}

output "node_group_id" {
  value = aws_eks_node_group.anushkachavan20.id
}

output "vpc_id" {
  value = aws_vpc.anushkachavan20_vpc.id
}

output "subnet_ids" {
  value = aws_subnet.anushkachavan20_subnet[*].id
}
