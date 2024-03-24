<p>请求查询资金账户，</p>
<p>响应: OnRspQryTradingAccount</p>
<span class="anchor" id="0ca338b3-1447-4dd3-9722-dbfceffa3a6a"></span>
## 1.函数原型
<p>virtual int ReqQryTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) = 0;</p>
<span class="anchor" id="56ecbbe5-add6-482f-9faf-3cf5516f02de"></span>
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
<span class="anchor" id="63383b84-8d5b-4e4e-9bff-635aa318ded9"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="12f0200f-d9f0-419f-94fa-85a8464ebcb1"></span>
## 4.调用示例
<pre><code>CThostFtdcQryTradingAccountField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqQryTradingAccount(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="c7a89390-f12d-4ff3-a406-868d33a48ce1"></span>
## 5.FAQ
<p>无</p>
