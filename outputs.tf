output "lambda_test_function_url" {
  description = "URL Lambda"
  value       = aws_lambda_function_url.test_lambda.function_url
}