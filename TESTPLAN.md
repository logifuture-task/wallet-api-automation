# Wallet API Test Plan

## 📌 Overview
This test plan outlines the **implemented** and **unimplemented** test cases for the Wallet API automation framework.

---

## ✅ **Implemented Test Cases**

### **1️⃣ Authentication Tests**
- **🔹 Valid Authentication** (`POST /user/login`) - Ensure a valid user receives a token.
- **🔹 Invalid Authentication** (`POST /user/login`) - Ensure invalid credentials return `401 Unauthorized`.

### **2️⃣ Wallet Management Tests**
- **🔹 Retrieve Wallet Details** (`GET /wallet/{walletId}`) - Fetch wallet information.
- **🔹 Nonexistent Wallet Access** (`GET /wallet/{walletId}`) - Requesting a non-existing wallet should return `404 Not Found`.
- **🔹 Unauthorized Wallet Access** (`GET /wallet/{walletId}`) - Attempting to access a wallet without authentication should return `401 Unauthorized`.

### **3️⃣ Transaction Processing Tests**
- **🔹 Process a Valid Transaction** (`POST /wallet/{walletId}/transaction`) - Ensure a valid deposit or withdrawal is processed correctly.
- **🔹 Retrieve a Specific Transaction** (`GET /wallet/{walletId}/transaction/{transactionId}`) - Fetch details of a specific transaction.
- **🔹 Retrieve All Transactions** (`GET /wallet/{walletId}/transactions`) - Retrieve all transactions for a wallet.
- **🔹 Transaction with Insufficient Funds** (`POST /wallet/{walletId}/transaction`) - Ensure an overdraft attempt is rejected with `400 Bad Request`.
- **🔹 Transaction with Invalid Currency** (`POST /wallet/{walletId}/transaction`) - Sending a transaction in an unsupported currency should return `400 Bad Request`.
- **🔹 Transaction with Negative Amount** (`POST /wallet/{walletId}/transaction`) - A transaction with a negative amount should be rejected.
- **🔹 Transaction with Excessively Large Amount** (`POST /wallet/{walletId}/transaction`) - A transaction with an unrealistic amount should return `400` or `422`.

### **4️⃣ Edge Cases**
- **🔹 Concurrent Transactions** (`POST /wallet/{walletId}/transaction`) - Ensure multiple transactions happening at the same time do not cause race conditions.
- **🔹 High-Frequency Transactions** (`POST /wallet/{walletId}/transaction`) - Ensure rate limiting is applied if many transactions are sent quickly.
- **🔹 Zero Amount Transactions** (`POST /wallet/{walletId}/transaction`) - A transaction with zero amount should be rejected.
- **🔹 Long Decimal Precision Amounts** (`POST /wallet/{walletId}/transaction`) - Transactions with excessive decimal places should be restricted.
- **🔹 Valid Maximum Decimal Precision** (`POST /wallet/{walletId}/transaction`) - Ensure transactions with allowed decimal precision are accepted.

---

## ❌ **Unimplemented but Important Test Cases**

### **1️⃣ Security & Authentication**
- **🔹 Token Expiry Handling** (`POST /user/login`) - Ensure expired tokens are rejected.
- **🔹 Token Reuse for Multiple Requests** (`POST /user/login`) - Validate that the same token can be used across multiple API calls until expiry.
- **🔹 Brute Force Attack Prevention** (`POST /user/login`) - Check rate-limiting for login attempts.

### **2️⃣ Wallet & Transaction Scenarios**
- **🔹 Transaction Reversal** (`PUT /wallet/{walletId}/transaction/{transactionId}/reversal`) - Simulate a refund or rollback process.
- **🔹 Cross-Currency Transactions** (`POST /wallet/{walletId}/transaction`) - Ensure transactions between different currencies are handled correctly.
- **🔹 Wallet Closure with Active Transactions** (`DELETE /wallet/{walletId}`) - Ensure wallets cannot be deleted if active transactions exist.

### **3️⃣ Performance & Load Testing**
- **🔹 Load Test for Transaction Processing** - Simulate thousands of transactions in a short period to test API stability.
- **🔹 Stress Testing on Authentication Service** - Check API response times under high user load.

---

## 🔥 **Prioritization of Unimplemented Cases**
| Test Case                          | Priority (High/Medium/Low) | Reason for Priority |
|-------------------------------------|----------------------------|---------------------|
| Token Expiry Handling               | High                       | Critical for security |
| Transaction Reversal                | High                       | Important for rollback mechanisms |
| Cross-Currency Transactions         | High                       | Affects multi-currency support |
| Brute Force Attack Prevention       | High                       | Ensures API security |
| Wallet Closure with Active Transactions | Medium                 | Improves user experience |
| Load Test for Transaction Processing | Medium                    | Ensures API scalability |
| Stress Testing on Authentication    | Medium                     | Verifies login stability |
