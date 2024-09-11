// src/services/v1/bookAPIService.js

import axios from 'axios'

const API_BASE_URL = process.env.VUE_APP_BACKEND_URL

export default {
  async fetchV1Books (url) {
    const finalUrl = url || `${API_BASE_URL}/book/v1/?page_size=8`

    try {
      const response = await axios.get(finalUrl)
      return response.data
    } catch (error) {
      console.error('Error fetching books:', error)
      throw error
    }
  }
}
