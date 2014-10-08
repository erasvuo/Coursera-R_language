myfunction <- function() {
	x <- rnorm(100)
	mean(x)
}

second <- function(x) {
	x + rnorm(length(x))
# comment added
}

third <- function(y) {
	y + rnorm(length(y))
# comment added
}