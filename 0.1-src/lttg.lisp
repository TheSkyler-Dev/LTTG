;; LTTG (Logic Truth Table Generator), (c) 2025 TheSkyler-Dev, Licensed under MIT License
;; initializer function
;; function to evaluate variables in the given logic expression
(defun eval-vars (expr)
  "Return a sorted list of unique single-letter variables in expression string"
  (let ((vars '()))
    (loop for c across expr 
      when (and (char>= c #\a) (char<= c #\z))
      do (pushnew (string c) vars :test #'string=))
      (sort vars #'string<)))

(defun truth-combos (vars)
  "Return alist of all possible values for VARS"
  (let* ((n (length vars)) (max (expt 2 n)))
    (loop for i from 0 below max
      collect (loop for j from 0 below n
        collect (cons (nth j vars)
          (if (logbitp (- n j 1) i) 1 0))))))

;; function to evaluate the logic expression
(defun eval-expr ())


;; function to generate the truth table for the given logic expression
(defun generate-TruthTable ())


;; function to print the truth table to the terminal
(defun print-TruthTable())


;; main function to run the program
(defun main ())


;; main function call
(main)