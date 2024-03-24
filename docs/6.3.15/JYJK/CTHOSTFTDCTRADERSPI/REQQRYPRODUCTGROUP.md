<p>请求查询产品组</p>
<p>响应: OnRspQryProductGroup</p>
<span class="anchor" id="27b1c71a-58c0-4e2b-b707-cefdd4ebff43"></span>
## 1.函数原型
<p>virtual int ReqQryProductGroup(CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID) = 0;</p>
<span class="anchor" id="f2a4ac43-2b75-4551-b425-e04fd27f92ee"></span>
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
<span class="anchor" id="9245c83c-466c-486b-8c56-b994487d12a3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b72a3365-c8f8-4b24-b907-a0ceabcfa251"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8c01f94a-f2cb-40be-9d56-abb6f3dd1b9b"></span>
## 5.FAQ
<p>无</p>
