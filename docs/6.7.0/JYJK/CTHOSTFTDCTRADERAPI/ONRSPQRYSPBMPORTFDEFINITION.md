<p>请求SPBM组合保证金套餐查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTERPARAMETER/">ReqQrySPBMInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="38814f89-6e6c-43a5-925d-4e8de0551d26"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMPortfDefinition(CThostFtdcSPBMPortfDefinitionField *pSPBMPortfDefinition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="189a7f68-545b-4220-bb18-023a830d084e"></span>
## 2.参数
<p>pSPBMPortfDefinition：组合保证金套餐</p>
<pre><code>struct CThostFtdcSPBMPortfDefinitionField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///组合保证金套餐代码
    TThostFtdcPortfolioDefIDType    PortfolioDefID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
    ///是否启用SPBM
    TThostFtdcBoolType  IsSPBM;
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
<span class="anchor" id="3f0a7311-1886-4358-ad37-a11dd29410d1"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e0cb135e-8a86-44bb-b8c8-27da9a8b5cb8"></span>
## 4.FAQ
<p>无</p>
