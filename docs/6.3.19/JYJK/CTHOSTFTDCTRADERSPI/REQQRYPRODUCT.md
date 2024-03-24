<p>请求查询产品</p>
<p>响应: OnRspQryProduct</p>
<span class="anchor" id="343a2b21-46dd-44d0-b129-3193c430854c"></span>
## 1.函数原型
<p>virtual int ReqQryProduct(CThostFtdcQryProductField *pQryProduct, int nRequestID) = 0;</p>
<span class="anchor" id="cee0d14a-0c15-453d-b1e5-7cb12faffc08"></span>
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
<span class="anchor" id="bffda1c1-ab2e-4180-8e91-3e1d39511515"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="e17e5cb4-c0e1-4618-9419-8342c63900e1"></span>
## 4.调用示例
<pre><code>CThostFtdcQryProductField a = { 0 };
strcpy_s(a.ProductID, "sc");
a.ProductClass = THOST_FTDC_PC_Futures;
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryProduct(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="aeaad594-8f10-4844-a50f-6194bc71250d"></span>
## 5.FAQ
<p>无</p>
