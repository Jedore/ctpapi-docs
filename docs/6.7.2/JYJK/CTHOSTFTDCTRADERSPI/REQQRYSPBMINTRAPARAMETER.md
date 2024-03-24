<p>请求SPBM品种内对锁仓折扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINTRAPARAMETER/">OnRspQrySPBMIntraParameter</a></p>
<span class="anchor" id="c7d27442-c0f8-4dac-bd13-029bc771a8ce"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMIntraParameter(CThostFtdcQrySPBMIntraParameterField *pQrySPBMIntraParameter, int nRequestID) = 0;</p>
<span class="anchor" id="9d5b6466-5368-46e6-8afc-c25bd2af5e7d"></span>
## 2.参数
<p>pQrySPBMIntraParameter：SPBM品种内对锁仓折扣参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="940f23bb-2250-43a9-a197-d3cf63a01a2e"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c0865f0d-3479-45c8-b581-4eaeab966606"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="c5a56df9-aa6f-4947-b858-7b9a871e4dc3"></span>
## 5.FAQ
<p>无</p>
