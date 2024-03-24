<p>订阅行情应答，调用SubscribeMarketData后，通过此接口返回。</p>
<span class="anchor" id="9b345495-532e-4a49-8fdb-a297a9d4e29c"></span>
## 1.函数原型
<p>virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e08cfa44-1b7a-465f-b597-c49804480424"></span>
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
<span class="anchor" id="5e891bac-9067-44d0-9876-804814e059ec"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ab5b603a-ea60-4158-b86f-492ee5dd33ed"></span>
## 4.FAQ
<p>无</p>
