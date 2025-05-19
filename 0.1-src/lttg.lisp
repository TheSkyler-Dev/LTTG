;; LTTG (Logic Truth Table Generator), (c) 2025 TheSkyler-Dev, Licensed under MIT License
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

;;Function to lispify operators
(defun lispify-ops (expr)
  "Replace AND, OR, NOT with Lisp equivalents in EXPR string"
  (let ((expr (string-upcase expr)))
    (setf expr (substitute #\Space #\Tab expr))
    (setf expr (replace-all expr "AND" "and"))
    (setf expr (replace-all expr "OR" "or"))
    (setf expr (replace-all expr "NOT" "not"))
    expr))

;;function to replace old operators with the lispified ones
(defun replace-all (str old new)
  "Replace all occurrences of OLD with NEW in STR"
  (with-output-to-string (out)
    (loop with oldlen = (length old)
      for i = 0 then j
      for j = (search old str :start2 i)
      do (write-string str out :start i :end (or j (length str)))
      when j do (write-string new out))
    ))

;; function to evaluate the logic expression
(defun eval-expr (expr var-vals)
  "Evaluate EXPR (string) with VAR_VALS ((var . val) list)."
  (let ((sexpr (read-from-string expr)))
    (eval `(let ,(mapcar (lambda (pair)
      (list (intern (string-upcase (car pair))) (cdr pair)))
      var-vals)
    ,sexpr))))


;; function to generate the truth table for the given logic expression
(defun generate-TruthTable (vars expr)
  "Return list of rows for the truth table."
  (let* ((lisp-expr (lispify-ops expr))
         (combos (truth-combos vars)))
    (mapcar (lambda (combo)
              (let ((result (eval-expr lisp-expr combo)))
                (append (mapcar #'cdr combo) (list (if result 1 0)))))
            combos)))


;; function to print the truth table to the terminal
(defun print-TruthTable(vars expr)
  (let ((table (generate-TruthTable vars expr)))
    (format t "~{~A~^ | ~}~%" (append vars (list "Result")))
    (format t "~A~%" (make-string (+ 4 (1+ (length vars))) :initial-element #\-))
    (dolist (row table)
      (format t "~{~A~^ | ~}~%" row))))


;; main function to run the program
(defun main ()
  (format t "Enter a boolean expression: ")
  (let* ((expr (read-line)) (vars (eval-vars expr)))
    (print-TruthTable vars expr)))

;; main function call
(main)
;;DOES NOT WORK -> Runs into Heap exhaustion, Lisp may not be suitable for the task at hand