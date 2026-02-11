// ============= AUTHENTICATION HELPERS =============

function checkAuth() {
    const token = localStorage.getItem('token');
    if (!token) {
        // Only redirect if not already on auth pages
        const pathname = window.location.pathname;
        if (pathname !== '/login' && pathname !== '/register') {
            window.location.href = '/login';
        }
    }
}

function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user_id');
    localStorage.removeItem('email');
    window.location.href = '/login';
}

function getAuthHeader() {
    const token = localStorage.getItem('token');
    return {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
    };
}

// ============= API CALL HELPERS =============

async function apiCall(endpoint, method = 'GET', data = null) {
    const options = {
        method: method,
        headers: getAuthHeader()
    };
    
    if (data) {
        options.body = JSON.stringify(data);
    }
    
    try {
        const response = await fetch(endpoint, options);
        
        if (response.status === 401) {
            logout();
            return null;
        }
        
        return await response.json();
    } catch (error) {
        console.error('API call error:', error);
        return null;
    }
}

// ============= UI HELPERS =============

function showLoading(elementId) {
    const el = document.getElementById(elementId);
    if (el) el.style.display = 'flex';
}

function hideLoading(elementId) {
    const el = document.getElementById(elementId);
    if (el) el.style.display = 'none';
}

function showMessage(elementId, message, type = 'error') {
    const el = document.getElementById(elementId);
    if (el) {
        el.textContent = message;
        el.className = `message ${type}`;
        el.style.display = 'block';
    }
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        alert('Copied to clipboard!');
    });
}

// ============= FORMAT HELPERS =============

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
}

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

// ============= VALIDATION =============

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validateForm(formData) {
    for (const [key, value] of Object.entries(formData)) {
        if (!value || value.toString().trim() === '') {
            return false;
        }
    }
    return true;
}

// ============= DOCUMENT READY =============

document.addEventListener('DOMContentLoaded', () => {
    // Add any global initialization here
    console.log('MarketAI Suite loaded');
});
