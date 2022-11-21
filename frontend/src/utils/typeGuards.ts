import { STATUS_CODES, SNACKBAR_MESSAGES } from '@/constants'

export const isStatusCode = (
  value: number
): value is keyof typeof SNACKBAR_MESSAGES => {
  return STATUS_CODES.includes(value)
}
