subroutine fortran_sum(a, m, n, sum)
implicit none
integer :: m,n
real*8  :: a(m,n), sum
!!!!!!!!!!!!!!!f2py!!!!!!!!!!!!!!!!!!!!!!!!!
!f2py real*8, intent(in)  ::  a(m, n)
!f2py integer, intent(in), optional, depend(a) :: m=shape(a,0)
!f2py integer, intent(in), optional, depend(a) :: n=shape(a,1)
!f2py real*8, intent(out)  ::  sum
integer :: i,j
do i=1,m
    do j=1,n
        sum = sum + a(i,j)
    end do
end do
end subroutine