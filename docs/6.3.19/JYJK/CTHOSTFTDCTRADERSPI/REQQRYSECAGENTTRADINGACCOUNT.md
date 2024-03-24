<p>请求查询资金账户</p>
<p>响应: OnRspQrySecAgentTradingAccount</p>
<span class="anchor" id="5e9cb016-fe9e-4cd3-8740-41b8ba7781b8"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) = 0;</p>
<span class="anchor" id="76393425-7aa9-4864-a476-9002864a0037"></span>
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
<span class="anchor" id="e5d7c73f-65ae-430c-bc81-19fbe6da6621"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6c66f000-3e84-4aa8-9a23-78bd80bd3c16"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="6f674154-501e-4b38-83b9-e0c3dbd6eb9d"></span>
## 5.FAQ
<p>无</p>
