<p>取消订阅行情应答，当UnSubscribeMarketData后，调用此接口。</p>
<span class="anchor" id="ad5aea1e-ec9e-4df0-8ae1-a9e344b327fd"></span>
## 1.函数原型
<p>virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="4025a2bf-8210-4b68-a7f6-2460c5eb6d31"></span>
## 2.参数
<p>pSpecificInstrument：指定的合约</p>
<pre><code>struct CThostFtdcSpecificInstrumentField
{
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="74aa7c1e-aa82-4f39-83fe-6ef138929fe8"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d45be0f8-dd31-4589-b6f0-09d989e5d9b6"></span>
## 4.FAQ
<p>无</p>
