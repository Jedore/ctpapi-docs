<p>订阅行情应答，调用SubscribeMarketData后，通过此接口返回。</p>
<span class="anchor" id="1b76bab9-a37f-41d5-9437-812087532d00"></span>
## 1.函数原型
<p>virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e5792eaf-b5e3-436f-b935-b343a8f60930"></span>
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
<span class="anchor" id="8d643b76-3adf-4990-901e-4cc7b6064145"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6815eb28-163f-4a2e-bf98-da4912cd3590"></span>
## 4.FAQ
<p>无</p>
