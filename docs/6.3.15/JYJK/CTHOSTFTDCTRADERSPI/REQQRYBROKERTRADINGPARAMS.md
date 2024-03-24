<p>请求查询经纪公司交易参数</p>
<p>响应: OnRspQryBrokerTradingParams</p>
<span class="anchor" id="3b85e157-7256-44c0-a751-21d42e0bbf76"></span>
## 1.函数原型
<p>virtual int ReqQryBrokerTradingParams(CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID) = 0;</p>
<span class="anchor" id="edae0bfe-9b4a-4fc2-8926-74b2e853f258"></span>
## 2.参数
<p>pQryBrokerTradingParams：查询经纪公司交易参数</p>
<pre><code>struct CThostFtdcQryBrokerTradingParamsField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="30179371-fab4-4fbd-af2f-d75c8e90db00"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0db51bde-cae6-4b9f-b51c-5310dc3583d4"></span>
## 4.调用示例
<pre><code>CThostFtdcQryBrokerTradingParamsField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryBrokerTradingParams(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="9cbe9101-14ac-4aef-8be1-28db62bf694f"></span>
## 5.FAQ
<p>无</p>
