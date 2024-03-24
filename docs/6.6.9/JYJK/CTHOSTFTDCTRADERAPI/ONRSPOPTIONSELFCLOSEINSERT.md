<p>期权自对冲录入请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>后，该方法被调用</p>
<span class="anchor" id="91405bd5-f62a-4bd6-ade6-62150da8b60d"></span>
## 1.函数原型
<p>virtual void OnRspOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, , bool bIsLast) {};</p>
<span class="anchor" id="4dcb113e-9530-45a6-9903-76b62a19db22"></span>
## 2.参数
<p>pInputOptionSelfClose：输入的期权自对冲</p>
<pre><code>struct CThostFtdcInputOptionSelfCloseField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///期权自对冲引用
    TThostFtdcOrderRefType  OptionSelfCloseRef;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///数量
    TThostFtdcVolumeType    Volume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType  BusinessUnit;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///期权行权的头寸是否自对冲
    TThostFtdcOptSelfCloseFlagType  OptSelfCloseFlag;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType    CurrencyID;
    ///交易编码
    TThostFtdcClientIDType  ClientID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve2;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
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
<span class="anchor" id="1373d079-88a9-43ec-9e06-7c8719895e4a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="62d57e90-ba2b-4cb0-b60d-d6ef165643a4"></span>
## 4.FAQ
<p>无</p>
