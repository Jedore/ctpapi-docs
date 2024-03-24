<span class="anchor" id="e35b1713-817d-449b-8403-9d0272c53373"></span>
## 1.说明
<p>请求查询报单手续费</p>
<p>响应: OnRspQryInstrumentOrderCommRate</p>
<span class="anchor" id="675d47d1-45d5-43ff-a912-5d81471b97fe"></span>
## 2.函数原型
<p>virtual int ReqQryInstrumentOrderCommRate(CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID) = 0;</p>
<span class="anchor" id="88f2fe24-247e-4220-b181-2d5802b77e9a"></span>
## 3.参数
<p>pQryInstrumentOrderCommRate：报单手续费率查询</p>
<pre><code>struct CThostFtdcQryInstrumentOrderCommRateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="e1859e8d-d989-4042-8827-8a1b07cb51bb"></span>
## 4.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="5738834a-1260-4dbb-b3ba-4a93d87c4f47"></span>
## 5.调用示例
<pre><code>CThostFtdcQryInstrumentOrderCommRateField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
strcpy(a.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqQryInstrumentOrderCommRate(&amp;a, 1);
</code></pre>
<span class="anchor" id="bfde4519-0458-41a9-ad0a-622b04b5058e"></span>
## 6.FAQ
<p>无</p>
