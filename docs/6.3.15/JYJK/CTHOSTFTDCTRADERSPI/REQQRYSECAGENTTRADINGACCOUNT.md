<p>请求查询资金账户</p>
<p>响应: OnRspQrySecAgentTradingAccount</p>
<span class="anchor" id="eb8c1438-d40e-4eb6-a3ec-809a4271008d"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) = 0;</p>
<span class="anchor" id="0e15e8ec-cac7-47e8-bb66-4b22a101b43a"></span>
## 2.参数
<p>pQryTradingAccount：请求查询资金账户</p>
<pre><code>struct CThostFtdcQryTradingAccountField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///业务类型
    TThostFtdcBizTypeType BizType;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="f2e5b280-ccbd-45da-8f2c-c0019bc9c0d5"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="cbf07707-e9cb-412b-b776-f94a1db19cae"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="c36b3f58-4247-4a02-bc18-fd95d0dd0e95"></span>
## 5.FAQ
<p>无</p>
