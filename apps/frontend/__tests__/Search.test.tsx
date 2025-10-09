
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import Search from '../components/Search'

// Mock the search results
const mockSearchResults = [
  {
    id: '1',
    title: 'First Article',
    slug: 'first-article',
    category: 'Technology'
  },
  {
    id: '2',
    title: 'Second Article',
    slug: 'second-article',
    category: 'Science'
  }
]

// Mock the search function
const mockSearch = jest.fn().mockResolvedValue(mockSearchResults)

jest.mock('../services/api', () => ({
  searchArticles: (query: string) => mockSearch(query)
}))

describe('Search Component', () => {
  beforeEach(() => {
    mockSearch.mockClear()
  })

  it('renders search input correctly', () => {
    render(<Search />)
    
    // Check if search input exists
    expect(screen.getByPlaceholderText(/search/i)).toBeInTheDocument()
  })

  it('displays search results after typing', async () => {
    render(<Search />)
    
    // Get the search input
    const searchInput = screen.getByPlaceholderText(/search/i)
    
    // Type in the search input
    await userEvent.type(searchInput, 'test')
    
    // Wait for search results to be displayed
    await waitFor(() => {
      expect(mockSearch).toHaveBeenCalledWith('test')
    })
    
    // Check if search results are displayed
    expect(screen.getByText('First Article')).toBeInTheDocument()
    expect(screen.getByText('Second Article')).toBeInTheDocument()
  })

  it('handles empty search results', async () => {
    // Mock empty search results
    mockSearch.mockResolvedValueOnce([])
    
    render(<Search />)
    
    // Get the search input
    const searchInput = screen.getByPlaceholderText(/search/i)
    
    // Type in the search input
    await userEvent.type(searchInput, 'nonexistent')
    
    // Wait for no results message
    await waitFor(() => {
      expect(screen.getByText(/no results found/i)).toBeInTheDocument()
    })
  })

  it('debounces search requests', async () => {
    jest.useFakeTimers()
    
    render(<Search />)
    
    // Get the search input
    const searchInput = screen.getByPlaceholderText(/search/i)
    
    // Type quickly
    await userEvent.type(searchInput, 'test')
    await userEvent.type(searchInput, 'testing')
    
    // Fast-forward timers
    jest.runAllTimers()
    
    // Should only call search once with final value
    expect(mockSearch).toHaveBeenCalledTimes(1)
    expect(mockSearch).toHaveBeenCalledWith('testing')
    
    jest.useRealTimers()
  })
})
