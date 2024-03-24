<p>请求查询产品组</p>
<p>响应: OnRspQryProductGroup</p>
<span class="anchor" id="489ddfa0-f908-43c6-a7fa-ed53ae38b72d"></span>
## 1.函数原型
<p>virtual int ReqQryProductGroup(CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID) = 0;</p>
<span class="anchor" id="bfd91356-069b-4a3c-9788-8374ec40a5eb"></span>
## 2.参数
<p>pQryProductGroup：查询产品组</p>
<pre><code>struct CThostFtdcQryProductGroupField
{
    ///产品代码
    TThostFtdcInstrumentIDType ProductID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="a3e9e391-8bad-497f-b563-50761eaebcce"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="e9e5aafd-701c-41ec-9e8c-fba694934dbf"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b0d24321-e986-4ae4-863c-2daed1c8e5d3"></span>
## 5.FAQ
<p>无</p>
