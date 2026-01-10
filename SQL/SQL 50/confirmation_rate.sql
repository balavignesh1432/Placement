-- Group by user id, for each group perform aggregation confirmation rate
-- Need to calculate confirmation out of total so use avg, as case when for 1 if true, 0 if false

select Signups.user_id, Round(avg(
    case
        when action = 'confirmed' then 1
        else 0
    end
)::numeric, 2) as confirmation_rate
from Signups left join Confirmations
on Signups.user_id=Confirmations.user_id
group by Signups.user_id;