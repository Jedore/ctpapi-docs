<p>请求查询合约手续费率，对应响应OnRspQryInstrumentCommissionRate。如果InstrumentID填空，则返回持仓对应的合约手续费率。</p>
<blockquote>
<p>目前无法通过一次查询得到所有合约手续费率，如果要查询所有，则需要通过多次查询得到。</p>
</blockquote>
<span class="anchor" id="8f7f6742-e4fd-475d-8163-dd655c62b261"></span>
## 1.函数原型
<p>virtual int ReqQryInstrumentCommissionRate(CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID) = 0;</p>
<span class="anchor" id="f5c2600d-4c3c-48fe-b064-a1c05aef2eda"></span>
## 2.参数
<p>pQryInstrumentCommissionRate：查询手续费率</p>
<pre><code>struct CThostFtdcQryInstrumentCommissionRateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>InstrumentID：返回手续费率对应的合约。</p>
<blockquote>
<p>但是如果在柜台没有设置具体合约的手续费率，则默认会返回产品的手续费率，InstrumentID就为对应产品ID。</p>
</blockquote>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="07c30f6a-296b-4863-979b-9d22e3bdfdfc"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="bfafb91a-97bf-4d7f-be94-9cb1fde77823"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInstrumentCommissionRateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqQryInstrumentCommissionRate(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="976a26fd-3cfc-4ddf-947e-62eb1b26eb3b"></span>
## 5.FAQ
<p>无</p>
