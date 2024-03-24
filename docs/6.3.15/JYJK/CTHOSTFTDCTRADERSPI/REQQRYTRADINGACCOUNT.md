<p>请求查询资金账户，</p>
<p>响应: OnRspQryTradingAccount</p>
<span class="anchor" id="957d4208-524e-44e2-8bcb-a5ed83ac0ec9"></span>
## 1.函数原型
<p>virtual int ReqQryTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) = 0;</p>
<span class="anchor" id="07cf2669-762e-46a1-b012-eba69b215afd"></span>
## 2.参数
<p>pQryTradingAccount：查询资金账户</p>
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
<span class="anchor" id="3fba3dd5-83d5-4358-a1b9-037029c0d409"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ec84ae12-323c-4714-b598-11c0f79717eb"></span>
## 4.调用示例
<pre><code>CThostFtdcQryTradingAccountField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqQryTradingAccount(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="3a02fd48-059f-40d2-b79e-965fa0cfb11c"></span>
## 5.FAQ
<p>无</p>
