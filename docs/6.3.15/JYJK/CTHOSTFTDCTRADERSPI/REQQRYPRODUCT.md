<p>请求查询产品</p>
<p>响应: OnRspQryProduct</p>
<span class="anchor" id="2ea05505-23d1-4488-9c8d-ace98118c5b5"></span>
## 1.函数原型
<p>virtual int ReqQryProduct(CThostFtdcQryProductField *pQryProduct, int nRequestID) = 0;</p>
<span class="anchor" id="9b219a5c-cde3-429a-b6f2-5c1593d16593"></span>
## 2.参数
<p>pQryProduct：查询产品</p>
<pre><code>struct CThostFtdcQryProductField
{
    ///产品代码
    TThostFtdcInstrumentIDType ProductID;
    ///产品类型
    TThostFtdcProductClassType ProductClass;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="d0aa7deb-aa87-4474-9f41-a5674d75a5da"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7a6b86f5-f889-4e11-acf7-0da7b28432c5"></span>
## 4.调用示例
<pre><code>CThostFtdcQryProductField a = { 0 };
strcpy_s(a.ProductID, "sc");
a.ProductClass = THOST_FTDC_PC_Futures;
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryProduct(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="14d3f47e-4a27-494f-b39d-b59deb8d2769"></span>
## 5.FAQ
<p>无</p>
