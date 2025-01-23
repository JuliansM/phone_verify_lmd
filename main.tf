resource "aws_iam_role" "test_lambda" {
  name               = "iam_for_lambda_py"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

#-- Logging
resource "aws_cloudwatch_log_group" "lambda_logging" {
  name              = "/aws/lambda/${local.lambda_name}"
  retention_in_days = 7
}

resource "aws_iam_policy" "lambda_logging" {
  name        = "lambda_logging"
  path        = "/"
  description = "IAM policy for logging from a lambda ${local.lambda_name}"
  policy      = data.aws_iam_policy_document.lambda_logging.json
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.test_lambda.name
  policy_arn = aws_iam_policy.lambda_logging.arn
}

#-- Lambda
resource "aws_lambda_function" "test_lambda" {
  filename      = local.zip_filename
  function_name = local.lambda_name
  role          = aws_iam_role.test_lambda.arn
  handler       = "index.handler"

  source_code_hash = data.archive_file.lambda.output_base64sha256

  runtime = "python3.13"

  logging_config {
    log_format = "Text"
  }

  depends_on = [ 
    aws_iam_role_policy_attachment.lambda_logs,
    aws_cloudwatch_log_group.lambda_logging
  ]
}

resource "aws_lambda_function_url" "test_lambda" {
  function_name      = aws_lambda_function.test_lambda.function_name
  authorization_type = "NONE"
}